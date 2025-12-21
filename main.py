import json
import textwrap

def define_env(env):
    @env.macro
    def viral_chart(id, options, height="400px"):
        json_options = json.dumps(options)

        html = f"""
        <div class="chart-wrapper" style="position: relative; width: 100%; max-width: 800px; margin: 0 auto;">
            
            <!-- BUTTON GROUP (Flexbox) -->
            <div style="position: absolute; top: 10px; right: 10px; z-index: 10; display: flex; gap: 8px;">
                
                <!-- 1. Copy URL Button (Grey/Secondary) -->
                <button class="md-button" 
                        onclick="copyPageUrl()"
                        title="Copy Page URL"
                        style="padding: 4px 10px; font-size: 0.7rem; min-width: auto; 
                               background-color: #f0f0f0; color: #333; border: 1px solid #ddd;">
                    🔗 Link
                </button>

                <!-- 2. Share Graph Button (Primary Blue) -->
                <button class="md-button md-button--primary" 
                        onclick="shareChart('{id}')"
                        style="padding: 4px 10px; font-size: 0.7rem; min-width: auto;">
                    📤 Share Graph
                </button>
            </div>
            
            <!-- Chart Container -->
            <div id="{id}" style="width: 100%; height: {height}; background-color: #fff; border-radius: 4px;"></div>
        </div>

        <script>
            window.addEventListener('load', function() {{
                renderOsintChart('{id}', {json_options});
            }});
        </script>
        """
        return textwrap.dedent(html)
