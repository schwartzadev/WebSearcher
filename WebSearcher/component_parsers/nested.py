def parse_nested(cmpt, sub_rank=0):
    """Parse the nested component. These are components that contain a main
    level result and then at least one sub result. The sub results are
    inside of an ul element.
    
    Args:
        cmpt (bs4 object): a nested component
    
    Returns:
        list: Return parsed dictionary in a list
    """

    parsed = {'type': 'nested', 'sub_rank':sub_rank}

    # item with a data-hveid attribute and a data-ved attribute
    main_item = cmpt.find('div', {'data-hveid': True, 'data-ved': True})

    parsed['title'] = main_item.find('h3').text
    parsed['url'] = main_item.find('a').attrs['href']
    parsed['cite'] = main_item.find('cite').text
    # TODO: add snippet/detail?

    # sub items
    # TODO: handle sub rank, etc. here?
    sub_items_container = cmpt.find('ul', {'class': 'FxLDp'})
    sub_items = sub_items_container.find_all('li')

    # FIXME: should this be named details instead?
    parsed['sub_items'] = []
    for sub_item in sub_items:
        parsed['sub_items'].append({
            'title': sub_item.find('h3').text,
            'url': sub_item.find('a').attrs['href'],
            'cite': sub_item.find('cite').text,
        })

    return [parsed]
