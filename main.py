def define_env(env):
    """
    This is the hook for defining variables, macros and filters.
    """
    @env.macro
    def viral_chart(id, height="400px"):
        """
        Generates the HTML for a chart with a built-in share button.
        Usage: {{ viral_chart('my-graph') }}
        """
        html = f"""
        <div class="chart-wrapper" style="position: relative; width: 100%; max-width: 800px; margin: 0 auto;">
            <!-- The Share Button -->
            <button class="md-button md-button--primary" 
                    onclick="shareChart('{id}')"
                    style="position: absolute; top: 10px; right: 10px; z-index: 10; 
                           padding: 4px 10px; font-size: 0.7rem; min-width: auto;">
                📤 Share Graph
            </button>
            
            <!-- The Chart Container -->
            <div id="{id}" style="width: 100%; height: {height}; background-color: #fff; border-radius: 4px;"></div>
        </div>
        """
        return html
