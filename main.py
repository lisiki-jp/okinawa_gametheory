import json
import textwrap

def define_env(env):
    @env.macro
    def viral_chart(id, options, height="500px"):
        json_options = json.dumps(options)

        # SVG Paths (Material Design Standard)
        icon_link = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill="currentColor" d="M3.9 12c0-1.71 1.39-3.1 3.1-3.1h4V7H7c-2.76 0-5 2.24-5 5s2.24 5 5 5h4v-1.9H7c-1.71 0-3.1-1.39-3.1-3.1zM8 13h8v-2H8v2zm9-6h-4v1.9h4c1.71 0 3.1 1.39 3.1 3.1s-1.39 3.1-3.1 3.1h-4V17h4c2.76 0 5-2.24 5-5s-2.24-5-5-5z"/></svg>'
        icon_share = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill="currentColor" d="M18 16.08c-.76 0-1.44.3-1.96.77L8.91 12.7c.05-.23.09-.46.09-.7s-.04-.47-.09-.7l7.05-4.11c.54.5 1.25.81 2.04.81a3 3 0 0 0 3-3 3 3 0 0 0-3-3 3 3 0 0 0-3 3c0 .24.04.47.09.7L8.04 9.81C7.5 9.31 6.79 9 6 9a3 3 0 0 0-3 3 3 3 0 0 0 3 3c.79 0 1.5-.31 2.04-.81l7.12 4.15c-.05.21-.08.43-.08.66 0 1.61 1.31 2.91 2.92 2.91s2.92-1.3 2.92-2.91a2.92 2.92 0 0 0-2.92-2.91"/></svg>'

        html = f"""
        <div class="chart-wrapper" style="position: relative; width: 100%; max-width: 800px; margin: 2em auto; border: 1px solid var(--md-default-fg-color--lightest); border-radius: 8px; overflow: hidden; background: #fff;">
            
            <!-- UNIFIED ACTION BUTTONS -->
            <div style="position: absolute; top: 12px; right: 12px; z-index: 10; display: flex; gap: 10px;">
                <button class="share-button chart-action-btn" onclick="copyPageUrl()" title="Copy Page Link">
                    {icon_link}
                </button>
                <button class="share-button chart-action-btn" onclick="shareChart('{id}')" title="Share this Graph">
                    {icon_share}
                </button>
            </div>
            
            <div id="{id}" class="lazy-chart" style="width: 100%; height: {height};"></div>
        </div>

        <script>
            window.osintChartData = window.osintChartData || {{}};
            window.osintChartData['{id}'] = {json_options};
        </script>
        """
        return textwrap.dedent(html)
