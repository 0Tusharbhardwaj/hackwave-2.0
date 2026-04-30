import re

def process(filename, keep_sections):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    secs = {
        'hero': ('<!-- Hero Section -->', '</header>'),
        'stats': ('<!-- Stats / Banner Section -->', '</div>\n  </div>'),
        'features': ('<!-- Features Section -->', '</section>'),
        'timeline': ('<!-- Timeline Section -->', '</section>'),
        'prizes': ('<!-- Prizes Section -->', '</section>'),
        'rules': ('<!-- Rules Section -->', '</section>'),
        'venue': ('<!-- Venue Section -->', '</section>'),
        'faq': ('<!-- FAQ Section -->', '</section>'),
        'sponsors': ('<!-- Sponsors Section -->', '</section>')
    }
    
    for sec, (start, end) in secs.items():
        if sec not in keep_sections:
            if sec == 'stats':
                content = re.sub(r'<!-- Stats / Banner Section -->.*?</div>\s*</div>', '', content, flags=re.DOTALL)
            elif sec == 'hero':
                content = re.sub(r'<!-- Hero Section -->.*?</header>', '', content, flags=re.DOTALL)
            else:
                content = re.sub(start + r'.*?</section>', '', content, flags=re.DOTALL)
    
    # Add top margin for secondary pages so navbar doesn't overlap
    if filename != 'index.html':
        content = content.replace('<section class="section', '<section class="section" style="margin-top: 100px; min-height: 70vh;"')
        
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

process('index.html', ['hero', 'stats', 'features', 'prizes', 'rules', 'venue'])
process('timeline.html', ['timeline'])
process('sponsors.html', ['sponsors'])
process('faqs.html', ['faq'])

print('done')
