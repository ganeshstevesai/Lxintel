import os
import re

css_files = [
    r"c:\Users\Admin\Pictures\all_project\Lxintel\Lxintel\static\index.css",
    r"c:\Users\Admin\Pictures\all_project\Lxintel\Lxintel\settlement\index.css",
    r"c:\Users\Admin\Pictures\all_project\Lxintel\Lxintel\Medical summary\index.css",
    r"c:\Users\Admin\Pictures\all_project\Lxintel\Lxintel\injury\index.css",
    r"c:\Users\Admin\Pictures\all_project\Lxintel\Lxintel\FAA_Medcert\index.css",
    r"c:\Users\Admin\Pictures\all_project\Lxintel\Lxintel\Demand QA\index.css",
    r"c:\Users\Admin\Pictures\all_project\Lxintel\Lxintel\demand Optimizer\index.css",
    r"c:\Users\Admin\Pictures\all_project\Lxintel\Lxintel\casevalue\index.css",
    r"c:\Users\Admin\Pictures\all_project\Lxintel\Lxintel\book_builder\index.css",
]

font_import = '@import url("https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;0,700;1,300;1,400&family=Montserrat:wght@300;400;500;600&display=swap");\n'

for file in css_files:
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Add font import if not exists
        if 'Cormorant+Garamond' not in content:
            content = font_import + '\n' + content
        
        # Change font color to #0d6efd
        # If it's static/index.css, change --text
        if 'static' in file and 'index.css' in file:
            content = re.sub(r'--text:\s*#[0-9a-fA-F]+;', '--text: #0d6efd;', content)
            content = re.sub(r'--text:\s*var\(--cyan\);', '--text: #0d6efd;', content)
        else:
            # Change color: #212529 or similar in body to #0d6efd
            content = re.sub(r'color:\s*#212529;', 'color: #0d6efd;', content)
            content = re.sub(r'color:\s*#111111;', 'color: #0d6efd;', content)
            content = re.sub(r'color:\s*#333(?:333)?;', 'color: #0d6efd;', content)
            content = re.sub(r'color:\s*#000(?:000)?;', 'color: #0d6efd;', content)

        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)

print("Updated fonts and colors across the application")
