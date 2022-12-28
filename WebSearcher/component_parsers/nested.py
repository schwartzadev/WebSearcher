def parse_nested(cmpt, sub_rank=0):
    """Parse the nested component
    
    Args:
        cmpt (bs4 object): a knowledge component
    
    Returns:
        list: Return parsed dictionary in a list
    """

    import pdb; pdb.set_trace()

    parsed = {'type': 'nested', 'sub_rank':sub_rank}
    details = {}

    # title_div = cmpt.find('div', {'class':'desktop-title-content'})
    # details['title'] = title_div.text if title_div else None

    # subtitle_span = cmpt.find('span', {'class':'desktop-title-subcontent'})
    # details['subtitle'] = subtitle_span.text if subtitle_span else None

    # img = cmpt.find('img', {'id':'lu_map'})
    # details['img_title'] = img.attrs['title'] if 'title' in img.attrs else None
    # parsed['details'] = details
    return [parsed]

    # return [parsed]
