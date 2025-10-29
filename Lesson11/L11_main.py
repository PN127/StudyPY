from typing import Dict, List, Optional

def format_post(posts: Dict[int, Dict[str, Optional[List[str]]]]) -> str:
    text = None
    tags_str = ''
    for id in posts:
        title_tag = posts[id]
        for title in title_tag:
            tags = title_tag[title]
            if tags is None:
                tags_str = ' -'
                continue
            for tag in tags:
                tags_str += tag + ', '   

        text = '['+ str(id) +']' + ' ' + title + ' - tags:' + tags_str
    print(text)            
    
def main():
    tags = ['tag1', 'tag2', 'tag3']
    titles = {'title': None}
    dic = {1: titles}
    format_post(dic)

main()