import os
import re

def kill_gradients(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. THE ULTIMATE GRADIENT KILLER FOR BUTTONS
    # We use background-image: none to ensure gradients are dead
    btn_hover_fix = """
/* KILL ALL GRADIENTS ON HOVER */
button:hover, 
.btn:hover, 
.btn-primary:hover, 
.login-btn:hover, 
.send-btn:hover, 
#process-btn:hover, 
#upload-new-files-btn:hover, 
.start-btn:hover, 
.new-chat-btn:hover, 
.dark-theme-btn-primary:hover {
    background-color: #0b5ed7 !important;
    background: #0b5ed7 !important;
    background-image: none !important;
    filter: none !important;
    box-shadow: none !important;
    transform: none !important;
}
"""

    if file_path.endswith('.css'):
        # Force body text to black and headers to blue
        content = re.sub(r'body,\s*html\s*\{([^}]*)color:\s*#0d6efd', r'body, html {\1color: #111111', content)
        content = re.sub(r'body\s*\{([^}]*)color:\s*#0d6efd', r'body {\1color: #111111', content)
        
        # Enforce blue headers in CaseValue-like Tailwind tags if they appear in CSS
        content = content.replace('text-[#111111]', 'text-[#0d6efd]')
        
        # Global radius removal
        content = re.sub(r'border-radius:[^;!]+(!important)?', 'border-radius: 0 !important', content)
        
        # Append fix
        content += btn_hover_fix

    if file_path.endswith('.html'):
        # Remove Tailwinds classes that might cause gradients or radius
        content = content.replace('rounded-lg', 'rounded-none')
        content = content.replace('rounded-xl', 'rounded-none')
        content = content.replace('rounded-2xl', 'rounded-none')
        content = content.replace('rounded-full', 'rounded-none')
        content = content.replace('shadow-lg', 'shadow-none')
        content = content.replace('bg-gradient-to-r', 'bg-[#0d6efd]')
        content = content.replace('from-blue-600', '')
        content = content.replace('to-blue-400', '')
        
        # Fix the specific headers found in CaseValue
        content = content.replace('text-[#111111]', 'text-[#0d6efd]')
        
        # Kill inline hover gradients if any
        content = re.sub(r'hover:bg-gradient-[^ ]+', 'hover:bg-[#0b5ed7]', content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

root_dir = r'c:\Users\Admin\Pictures\all_project\Lxintel\Lxintel'
for root, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith(('.html', '.css')):
            kill_gradients(os.path.join(root, file))

print('Gradient killer executed. All buttons normalized to solid blue on hover across all panels.')
