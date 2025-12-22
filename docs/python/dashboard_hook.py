import os
import re

def on_page_markdown(markdown, page, config, files):
    if page.file.src_path != 'index.md':
        return markdown

    docs_dir = config['docs_dir']
    dashboard_items = []
    toc_lines = []
    sorted_files = sorted(files, key=lambda f: f.src_path)
    
    for f in sorted_files:
        if f.src_path == 'index.md': continue
            
        file_path = os.path.join(docs_dir, f.src_path)
        with open(file_path, 'r', encoding='utf-8') as open_file:
            content = open_file.read()

        # --- A. TOC LOGIC (Unchanged) ---
        lines = content.split('\n')
        for line in lines:
            if line.startswith('# '):
                title = line.replace('# ', '').strip()
                toc_lines.append(f"- [{title}]({f.url})")
            elif line.startswith('## '):
                sub_title = line.replace('## ', '').strip()
                anchor = sub_title.lower().replace(' ', '-').replace('?', '').replace(':', '')
                toc_lines.append(f"    - [{sub_title}]({f.url}#{anchor})")

        # --- B. EXTRACT CHARTS ---
        chart_matches = re.findall(r"\{\{\s*viral_chart\s*\(\s*['\"](.*?)['\"]\s*,\s*([^,\)]+)(.*?)\)\s*\}\}", content)
        
        for (chart_id, var_name, extra_args) in chart_matches:
            home_id = f"home_{chart_id}"
            
            # We wrap the macro in 'homepage-chart-wrapper'
            injected_macro = f"""
<div class="grid-item">
    <div class="homepage-chart-wrapper">
        {{{{ viral_chart('{home_id}', {var_name}{extra_args}) }}}}
        <p class="caption">
            <a href="{f.url}">View full size in: {f.page.title if f.page else f.src_path}</a>
        </p>
    </div>
</div>
"""
            dashboard_items.append(injected_macro)

    full_toc = "\n".join(toc_lines)
    full_dashboard = '<div class="grid cards" markdown>\n' + "\n".join(dashboard_items) + "\n</div>"

    markdown = markdown.replace('{{ ALL_CHARTS }}', full_dashboard)
    markdown = markdown.replace('{{ GLOBAL_TOC }}', full_toc)

    return markdown
