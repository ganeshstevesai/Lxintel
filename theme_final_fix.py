import os
import re

def final_theme_fix(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. BUTTONS: Simple blue bg, white text, no shadow, no radius
    # We'll target common button classes and tags
    button_styles = """
button, .btn, .btn-primary, .login-btn, .send-btn, #process-btn, #upload-new-files-btn, .start-btn, .new-chat-btn {
    background-color: #0d6efd !important;
    background: #0d6efd !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 0 !important;
    box-shadow: none !important;
    text-shadow: none !important;
    font-family: "Montserrat", sans-serif !important;
    font-weight: 600 !important;
    text-transform: uppercase !important;
    cursor: pointer !important;
}
button:hover, .btn:hover {
    background-color: #0b5ed7 !important;
    background: #0b5ed7 !important;
    box-shadow: none !important;
    transform: none !important;
}
"""
    # If it's a CSS file, append or replace button rules
    if file_path.endswith('.css'):
        # Remove existing button rules that might conflict
        content = re.sub(r'button,.*?\{[^}]*\}', '', content, flags=re.DOTALL)
        content += button_styles
        
        # 2. HEADINGS: Blue
        content = re.sub(r'(h1|h2|h3|h4|h5|h6)\s*\{([^}]*color:\s*)[^;]+', r'\1 {\2#0d6efd', content)
        content = re.sub(r'(\.card-title|\.header-title h1|\.detail-title)\s*\{([^}]*color:\s*)[^;]+', r'\1 {\2#0d6efd', content)
        
        # 3. BODY TEXT: Black
        content = re.sub(r'(p|li|td|th|span|div)\s*\{([^}]*color:\s*)#0d6efd', r'\1 {\2#111111', content)
        content = content.replace('color: #0d6efd !important; } p, li, td, th, span, div', 'color: #111111 !important; } p, li, td, th, span, div')
        
        # 4. GLOBAL SHADOW REMOVAL
        content = re.sub(r'box-shadow:[^;]+', 'box-shadow: none !important', content)
        content = re.sub(r'text-shadow:[^;]+', 'text-shadow: none !important', content)
        content = content.replace('border-radius: 6px', 'border-radius: 0')
        content = content.replace('border-radius: 8px', 'border-radius: 0')
        content = content.replace('border-radius: 10px', 'border-radius: 0')
        content = content.replace('border-radius: 12px', 'border-radius: 0')
        content = content.replace('border-radius: 16px', 'border-radius: 0')

    # 5. HTML INLINE FIXES
    if file_path.endswith('.html'):
        # Fix inline buttons
        content = re.sub(r'style="([^"]*)background-color:\s*[^;]+', r'style="\1background-color: #0d6efd', content)
        content = re.sub(r'style="([^"]*)border-radius:\s*[^;]+', r'style="\1border-radius: 0', content)
        content = re.sub(r'style="([^"]*)box-shadow:\s*[^;]+', r'style="\1box-shadow: none', content)
        
        # Fix broken hex in HTML
        content = content.replace('#111ffffff', '#ffffff')
        content = content.replace('#111fff', '#ffffff')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

root_dir = r'c:\Users\Admin\Pictures\all_project\Lxintel\Lxintel'
for root, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith(('.html', '.css')):
            final_theme_fix(os.path.join(root, file))

print('Final theme alignment complete: Blue buttons (no radius), Blue headings, Black text, No shadows.')
