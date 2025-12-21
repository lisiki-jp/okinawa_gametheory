import textwrap  # <--- Import this

def define_env(env):
    @env.macro
    def viral_chart(id, height="400px"):
        # The indentation inside this string is what broke it.
        # We use textwrap.dedent() to remove it automatically.
        html = f"""
        <div class="chart-wrapper" style="position: relative; width: 100%; max-width: 800px; margin: 0 auto;">
            <button class="md-button md-button--primary" 
                    onclick="shareChart('{id}')"
                    style="position: absolute; top: 10px; right: 10px; z-index: 10; 
                           padding: 4px 10px; font-size: 0.7rem; min-width: auto;">
                📤 Share Graph
            </button>
            <div id="{id}" style="width: 100%; height: {height}; background-color: #fff; border-radius: 4px;"></div>
        </div>
        """
        return textwrap.dedent(html)  # <--- This fixes the "Code Block" issue
