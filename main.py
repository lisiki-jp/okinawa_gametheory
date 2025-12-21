import json
import textwrap

def define_env(env):
    @env.macro
    def viral_chart(id, options, height="400px"):
        """
        Generates a Chart + Share Button + Script automatically.
        args:
            id: Unique HTML ID for the chart.
            options: A Python dictionary of ECharts options.
            height: Height of the chart (default 400px).
        """
        # Convert the Python Dictionary to a JSON string for JavaScript
        json_options = json.dumps(options)

        html = f"""
        <div class="chart-wrapper" style="position: relative; width: 100%; max-width: 800px; margin: 0 auto;">
            <!-- Share Button -->
            <button class="md-button md-button--primary" 
                    onclick="shareChart('{id}')"
                    style="position: absolute; top: 10px; right: 10px; z-index: 10; 
                           padding: 4px 10px; font-size: 0.7rem; min-width: auto;">
                📤 Share Graph
            </button>
            
            <!-- Chart Container -->
            <div id="{id}" style="width: 100%; height: {height}; background-color: #fff; border-radius: 4px;"></div>
        </div>

        <!-- Auto-Generated Script -->
        <script>
            window.addEventListener('load', function() {{
                // Relies on the helper function we made in chart_share.js
                renderOsintChart('{id}', {json_options});
            }});
        </script>
        """
        return textwrap.dedent(html)
