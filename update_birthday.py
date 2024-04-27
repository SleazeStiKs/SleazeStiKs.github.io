import pathlib
import re
from datetime import date

root = pathlib.Path(__file__).parent.resolve()


def replace_writing(content, marker, chunk, inline=False):
    r = re.compile(
        r'<!\-\- {} starts \-\->.*<!\-\- {} ends \-\->'.format(marker, marker),
        re.DOTALL,
    )
    if not inline:
        chunk = '\n{}\n'.format(chunk)
    chunk = '<!-- {} starts -->{}<!-- {} ends -->'.format(marker, chunk, marker)
    return r.sub(chunk, content)

def calculateAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))

    return age

if __name__ == '__main__':
    readme_path = root / 'src/pages/index.astro'
    readme = readme_path.open().read()
    
    # Update Age
    rewritten_count = replace_writing(readme, 'age', calculateAge(date(2005, 4, 3)), inline=True)
    readme_path.open('w').write(rewritten_count)


    readme_path = root / 'src/pages/about.astro'
    readme = readme_path.open().read()
    
    # Update Age
    rewritten_count = replace_writing(readme, 'age', calculateAge(date(2005, 4, 3)), inline=True)
    readme_path.open('w').write(rewritten_count)