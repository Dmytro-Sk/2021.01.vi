class Locators:

    """Page 1"""
    
    # main locators
    NAME = './/td[@class="default"]//a[@class="hnuser"]/text()'
    PERSON_ID = './@id'
    LOCATION = r'(Location: )(.+)(\n)'
    REMOTE = r'(Remote: )(.+)(\n)'
    WILLING_TO_RELOCATE = r'(Willing to relocate:)(.+)(\n)'
    TECHNOLOGIES = r'(Technologies: )(.+)(\n)'
    CV_LINK = r'(Résumé/CV: |Resume: )(.+)(\n)'
    # CV_LINK = r'https?://(www\.)?(\w+)(\.\w+)'
    EMAIL = r'(Email: )(.+)(\n)|[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    # EMAIL = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    # LINKEDIN = r'(LinkedIn: )(.+)(\n)'
    # LINKEDIN = r'(https?://)?(\w+?\.)?(linkedin.com)(/\w+)?(/\w+)?'
    LINKEDIN = r'https?://\w+\.linkedin.com/\w+/\w+'
    ABOUT = ''

    # additional locators
    COMMENTS = '//tr[@class="athing comtr "]'
    TEXT = '(//tr[@class="athing comtr "])[2]//span[@class="commtext c00"]//text()'

    """Page 2"""
    
    # main locators
    
    # additional locators
