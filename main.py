def text_to_flow(text: str):
    # Split sentences
    parts = [p.strip() for p in text.replace("Then", ".").split(".") if p.strip()]

    nodes = parts
    edges = []

    for i in range(len(nodes) - 1):
        edges.append([nodes[i], nodes[i + 1]])

    return {
        "nodes": nodes,
        "edges": edges
    }


if __name__ == "__main__":
    print("Enter an explanation:")
    user_input = input("> ")

    flow = text_to_flow(user_input)

    print("\nGenerated Flow:")
    print(flow)
