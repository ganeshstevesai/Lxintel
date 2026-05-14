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

proper_global_styles = """
/* Global Font & Color Overrides */
@import url("https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;0,700;1,300;1,400&family=Montserrat:wght@300;400;500;600&display=swap");

body, html, p, span, div, li, td, th {
    font-family: "Montserrat", sans-serif !important;
    color: #111111;
}

input, textarea, select, .form-control, input[type="text"], input[type="email"], input[type="file"] {
    background-color: #ffffff !important;
    color: #111111 !important;
    border: 1px solid #dee2e6 !important;
    font-family: "Montserrat", sans-serif !important;
}

input::placeholder, textarea::placeholder {
    color: #6c757d !important;
}

label, .billing-label {
    font-family: "Montserrat", sans-serif !important;
    color: #111111 !important;
    font-weight: 600;
}

h1, h2, h3, h4, h5, h6, .card-title, .header-title h1, .topbar-logo span {
    font-family: "Cormorant Garamond", serif !important;
    color: #0d6efd !important;
}

button, .btn, .btn-primary, .dark-theme-btn-primary, .login-btn, .send-btn {
    font-family: "Montserrat", sans-serif !important;
    background: linear-gradient(135deg, #0d6efd, #0b5ed7) !important;
    color: #ffffff !important;
    border: 2px solid rgba(13, 110, 253, 0.6) !important;
    border-radius: 6px !important;
    font-weight: bold !important;
    text-transform: uppercase;
    letter-spacing: 1px;
    box-shadow: 0 0 18px rgba(13, 110, 253, 0.6) !important;
    transition: 0.25s ease-in-out !important;
}

button:hover:not(:disabled), .btn:hover:not(:disabled), .btn-primary:hover:not(:disabled), .dark-theme-btn-primary:hover:not(:disabled), .login-btn:hover:not(:disabled), .send-btn:hover:not(:disabled) {
    background: linear-gradient(135deg, #0b5ed7, #0a58ca) !important;
    box-shadow: 0 0 28px rgba(13, 110, 253, 0.9) !important;
    transform: translateY(-2px) !important;
}

button:disabled, .btn:disabled, .btn-primary:disabled {
    background: #cccccc !important;
    color: #666666 !important;
    border-color: #bbbbbb !important;
    box-shadow: none !important;
    cursor: not-allowed !important;
    transform: none !important;
}

a {
    color: #0d6efd !important;
    font-family: "Montserrat", sans-serif;
    text-decoration: none;
}

a:hover {
    color: #0b5ed7 !important;
}

.card, .glass-panel, .dark-theme-card, .login-form-card, .item-card {
    background: #ffffff !important;
    border: 1px solid #dee2e6 !important;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.05) !important;
    color: #111111 !important;
}
"""

for file in css_files:
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Remove old overrides if any exist
        content = re.sub(r'/\* Global Font & Color Overrides \*/.*', '', content, flags=re.DOTALL)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content.strip() + '\n\n' + proper_global_styles)

print("Applied strict blue/black light theme, fixed inputs and headings")
