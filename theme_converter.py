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

replacements = [
    (r'#111(?![0-9a-fA-F])', '#f8f9fa'),
    (r'#000(?![0-9a-fA-F])', '#ffffff'),
    (r'#000000', '#ffffff'),
    (r'#05101a', '#ffffff'),
    (r'#4dd2ff', '#0d6efd'),
    (r'rgba\(0,\s*0,\s*0,', 'rgba(255, 255, 255,'),
    (r'rgba\(17,\s*17,\s*17,', 'rgba(248, 249, 250,'),
    (r'#333(?![0-9a-fA-F])', '#dee2e6'),
    (r'#444(?![0-9a-fA-F])', '#ced4da'),
    (r'color:\s*#fff;', 'color: #212529;'),
    (r'color:\s*#eee;', 'color: #212529;'),
    (r'color:\s*#ddd;', 'color: #495057;'),
    (r'color:\s*#aaa;', 'color: #6c757d;'),
    (r'#1ab2ff', '#0b5ed7'),
    (r'#1a1a1a', '#f1f3f5'),
    (r'#222(?![0-9a-fA-F])', '#f8f9fa'),
]

for file in css_files:
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        for pat, repl in replacements:
            content = re.sub(pat, repl, content)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
print("Updated CSS files to light theme")
