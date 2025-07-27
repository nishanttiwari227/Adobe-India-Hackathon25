def build_hierarchy(flat):
    tree = []
    h1_node, h2_node = None, None

    for item in flat:
        level = item["level"]
        node = {k: item[k] for k in ("level", "text", "page")}
        node["children"] = []

        if level == "H1":
            tree.append(node)
            h1_node = node
            h2_node = None
        elif level == "H2":
            if h1_node:
                h1_node["children"].append(node)
                h2_node = node
            else:
                tree.append(node)
        elif level == "H3":
            if h2_node:
                h2_node["children"].append(node)
            elif h1_node:
                h1_node["children"].append(node)
            else:
                tree.append(node)

    return tree
