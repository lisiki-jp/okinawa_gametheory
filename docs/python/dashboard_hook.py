import os
import re

def on_page_markdown(markdown, page, config, files):
    # Only run this logic on the homepage (index.md)
    if page.file.src_path != 'index.md':
        return markdown

    # --- 1. SETUP VARIABLES ---
    docs_dir = config['docs_dir']
    dashboard_items = [] # Stores the chart HTML strings
    toc_lines = []
    
    # Sort files to ensure logical order
    sorted_files = sorted(files, key=lambda f: f.src_path)
    
    # --- 2. SCAN FILES ---
    for f in sorted_files:
        if f.src_path == 'index.md':
            continue
            
        file_path = os.path.join(docs_dir, f.src_path)
        with open(file_path, 'r', encoding='utf-8') as open_file:
            content = open_file.read()

        # --- A. BUILD GLOBAL TOC (Same as before) ---
        lines = content.split('\n')
        for line in lines:
            if line.startswith('# '):
                title = line.replace('# ', '').strip()
                toc_lines.append(f"- [{title}]({f.url})")
            elif line.startswith('## '):
                sub_title = line.replace('## ', '').strip()
                anchor = sub_title.lower().replace(' ', '-').replace('?', '').replace(':', '')
                toc_lines.append(f"    - [{sub_title}]({f.url}#{anchor})")

        # --- B. EXTRACT VIRAL CHARTS ---
        # Regex to find: {{ viral_chart('ID', VARIABLE) }}
        # Group 1: Chart ID (quoted)
        # Group 2: The Variable Name (e.g., test2)
        # Group 3: Optional extra args (ignored for now)
        chart_matches = re.findall(r"\{\{\s*viral_chart\s*\(\s*['\"](.*?)['\"]\s*,\s*([^,\)]+)(.*?)\)\s*\}\}", content)
        
        for (chart_id, var_name, extra_args) in chart_matches:
            # We create a NEW unique ID for the homepage so it doesn't conflict with the original page
            home_id = f"home_{chart_id}"
            
            # We construct a new Macro Call string to inject into index.md
            # We wrap it in a grid-item div for styling
            # We add a link back to the source chapter
            injected_macro = f"""
<div class="grid-item">
    <div class="chart-container">
        <!-- Re-calling the macro with the new ID -->
        {{{{ viral_chart('{home_id}', {var_name}{extra_args}) }}}}
        <p class="caption">
            Source: <a href="{f.url}">{f.page.title if f.page else f.src_path}</a>
        </p>
    </div>
</div>
"""
            dashboard_items.append(injected_macro)

    # --- 3. INJECT INTO HOME PAGE ---
    full_toc = "\n".join(toc_lines)
    
    # Wrap charts in your Grid Div
    full_dashboard = '<div class="grid cards" markdown>\n' + "\n".join(dashboard_items) + "\n</div>"

    markdown = markdown.replace('{{ ALL_CHARTS }}', full_dashboard)
    markdown = markdown.replace('{{ GLOBAL_TOC }}', full_toc)

    return markdown
