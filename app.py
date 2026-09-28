from flask import Flask, render_template_string

app = Flask(__name__)

# Enterprise-grade frontend using Tailwind CSS
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Enterprise CI/CD Dashboard</title>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/tailwindcss/2.2.19/tailwind.min.css" rel="stylesheet">
    <style>
        body { background-color: #0f172a; color: #f8fafc; font-family: ui-sans-serif, system-ui, sans-serif; }
        .glass-panel { background: rgba(30, 41, 59, 0.7); backdrop-filter: blur(10px); border: 1px solid #334155; }
        .glow-text { text-shadow: 0 0 10px rgba(56, 189, 248, 0.4); }
    </style>
</head>
<body class="min-h-screen flex items-center justify-center p-6">
    <div class="glass-panel rounded-2xl shadow-2xl p-10 max-w-4xl w-full">
        <div class="flex items-center justify-between border-b border-gray-700 pb-6 mb-6">
            <div>
                <h1 class="text-3xl font-bold text-sky-400 glow-text">Infrastructure Operations</h1>
                <p class="text-gray-400 mt-1">Automated CI/CD Deployment Pipeline Dashboard</p>
            </div>
            <div class="text-right">
                <span class="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-emerald-900 text-emerald-300 border border-emerald-700">
                    <svg class="mr-1.5 h-2 w-2 text-emerald-400" fill="currentColor" viewBox="0 0 8 8"><circle cx="4" cy="4" r="3" /></svg>
                    Pipeline Active
                </span>
            </div>
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
            <div class="bg-gray-800 rounded-lg p-5 border border-gray-700 shadow-inner">
                <h3 class="text-gray-400 text-xs uppercase tracking-wider mb-2">Build Environment</h3>
                <p class="text-lg font-semibold text-white">AWS EC2 (Ubuntu)</p>
            </div>
            <div class="bg-gray-800 rounded-lg p-5 border border-gray-700 shadow-inner">
                <h3 class="text-gray-400 text-xs uppercase tracking-wider mb-2">Orchestration</h3>
                <p class="text-lg font-semibold text-white">Kubernetes Cluster</p>
            </div>
            <div class="bg-gray-800 rounded-lg p-5 border border-gray-700 shadow-inner">
                <h3 class="text-gray-400 text-xs uppercase tracking-wider mb-2">Registry Target</h3>
                <p class="text-lg font-semibold text-white">sohamdocker25</p>
            </div>
        </div>

        <div class="bg-blue-900 bg-opacity-20 border-l-4 border-blue-500 p-4 rounded-r-lg mb-6">
            <div class="flex">
                <div class="flex-shrink-0">
                    <svg class="h-5 w-5 text-blue-400" viewBox="0 0 20 20" fill="currentColor">
                        <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clip-rule="evenodd" />
                    </svg>
                </div>
                <div class="ml-3">
                    <h3 class="text-sm font-medium text-blue-300">Deployment Verification Successful</h3>
                    <div class="mt-2 text-sm text-blue-200">
                        <p>Web application successfully containerized, tested, and rolled out via Jenkins automation.</p>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="border-t border-gray-700 pt-6 flex justify-between items-center text-sm text-gray-500">
            <p>Systems Administrator: <strong class="text-gray-300">Soham Sarkar</strong></p>
            <p>Evaluation & Sign-off: <strong class="text-gray-300">Linsa Chechi</strong></p>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
