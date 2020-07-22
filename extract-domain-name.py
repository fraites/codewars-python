# Test Cases
# domain_name("http://google.co.jp") => google
# domain_name("http://github.com/carbonfive/raygun") => "github" 
# domain_name("http://www.zombie-bites.com") => "zombie-bites"
# domain_name("https://www.cnet.com") => "cnet"

import re
def domain_name(url):
    domain = re.search(r'(https?://)?(www\.)?(?P<domain>[\w-]+)\.',url).group('domain')
    return domain
    
