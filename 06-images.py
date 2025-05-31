import os

from graphviz import Digraph

# Crea la directory images se non esiste
if not os.path.exists("images"):
    os.makedirs("images")


def setup_digraph(comment_text):
    dot = Digraph(comment=comment_text)
    dot.attr(bgcolor="transparent")  # Sfondo trasparente per LaTeX
    dot.attr(
        "node",
        shape="box",
        style="filled,rounded",
        fillcolor="#323232",
        fontcolor="#E6E6E6",
        color="#E6E6E6",
        fontname="Helvetica",
    )
    dot.attr("edge", color="#9696DC", fontcolor="#E6E6E6", fontname="Helvetica")
    return dot


def generate_ecb_diagram():
    dot = setup_digraph("ECB Mode")
    dot.graph_attr["rankdir"] = "TB"

    with dot.subgraph(name="cluster_enc") as c:
        c.attr(
            label="ECB Encryption (Blocco Singolo)",
            fontcolor="#E6E6E6",
            color="#E6E6E6",
        )
        c.node("P1_enc", "P1")
        c.node("E_enc", "Encrypt (K)")
        c.node("C1_enc", "C1")
        c.edge("P1_enc", "E_enc")
        c.edge("E_enc", "C1_enc")

    with dot.subgraph(name="cluster_dec") as c:
        c.attr(
            label="ECB Decryption (Blocco Singolo)",
            fontcolor="#E6E6E6",
            color="#E6E6E6",
        )
        c.node("C1_dec", "C1")
        c.node("D_dec", "Decrypt (K)")
        c.node("P1_dec", "P1")
        c.edge("C1_dec", "D_dec")
        c.edge("D_dec", "P1_dec")

    dot.render("images/ecb_mode_generated", format="png", cleanup=True)
    print("Generated images/ecb_mode_generated.png")


def generate_cbc_encryption_diagram():
    dot = setup_digraph("CBC Encryption")
    dot.graph_attr["rankdir"] = "TB"

    dot.node("IV", "IV", shape="parallelogram")
    dot.node("P1", "P1")
    dot.node(
        "XOR1",
        "XOR",
        shape="circle",
        width="0.5",
        height="0.5",
        fixedsize="true",
        fontsize="20",
        fillcolor="#326496",
    )
    dot.node("E1", "Encrypt (K)")
    dot.node("C1", "C1")

    dot.edge("IV", "XOR1")
    dot.edge("P1", "XOR1")
    dot.edge("XOR1", "E1")
    dot.edge("E1", "C1")

    dot.node("P2", "P2")
    dot.node(
        "XOR2",
        "XOR",
        shape="circle",
        width="0.5",
        height="0.5",
        fixedsize="true",
        fontsize="20",
        fillcolor="#326496",
    )
    dot.node("E2", "Encrypt (K)")
    dot.node("C2", "C2")

    dot.edge("C1", "XOR2", constraint="false")  # constraint false per layout
    dot.edge("P2", "XOR2")
    dot.edge("XOR2", "E2")
    dot.edge("E2", "C2")

    # Add invisible edges for ranking if needed for complex layouts
    # dot.edge('P1', 'P2', style='invis')
    # dot.edge('C1', 'C2', style='invis')

    dot.render("images/cbc_encryption_generated", format="png", cleanup=True)
    print("Generated images/cbc_encryption_generated.png")


def generate_ctr_mode_diagram():
    dot = setup_digraph("CTR Mode Encryption")
    dot.graph_attr["rankdir"] = "TB"

    dot.node("NonceCtr1", "Nonce+Counter1", shape="parallelogram")
    dot.node("E1", "Encrypt (K)")
    dot.node("Keystream1", "Keystream Block 1", shape="parallelogram")
    dot.node("P1", "P1")
    dot.node(
        "XOR1",
        "XOR",
        shape="circle",
        width="0.5",
        height="0.5",
        fixedsize="true",
        fontsize="20",
        fillcolor="#326496",
    )
    dot.node("C1", "C1")

    dot.edge("NonceCtr1", "E1")
    dot.edge("E1", "Keystream1")
    dot.edge("Keystream1", "XOR1")
    dot.edge("P1", "XOR1")
    dot.edge("XOR1", "C1")

    # Blocco 2
    dot.node("NonceCtr2", "Nonce+Counter2", shape="parallelogram")
    dot.node("E2", "Encrypt (K)")
    dot.node("Keystream2", "Keystream Block 2", shape="parallelogram")
    dot.node("P2", "P2")
    dot.node(
        "XOR2",
        "XOR",
        shape="circle",
        width="0.5",
        height="0.5",
        fixedsize="true",
        fontsize="20",
        fillcolor="#326496",
    )
    dot.node("C2", "C2")

    dot.edge("NonceCtr2", "E2")
    dot.edge("E2", "Keystream2")
    dot.edge("Keystream2", "XOR2")
    dot.edge("P2", "XOR2")
    dot.edge("XOR2", "C2")

    dot.render("images/ctr_mode_generated", format="png", cleanup=True)
    print("Generated images/ctr_mode_generated.png")


if __name__ == "__main__":
    generate_ecb_diagram()
    generate_cbc_encryption_diagram()
    generate_ctr_mode_diagram()
    # Potresti aggiungere qui le chiamate per generare diagrammi CFB e OFB
    # ma diventano più complessi con i registri a scorrimento e la selezione dei bit
    # print("\n--- Nota ---")
    # print("I diagrammi generati sono versioni semplificate.")
    # print(
    #     "Per diagrammi dettagliati come nelle slide, si consiglia di usare le immagini delle slide stesse."
    # )
    # print(
    #     "Nel documento LaTeX, assicurati che i percorsi in \\includegraphics puntino ai file corretti"
    # )
    # print(
    #     "(es. slide_X.png se usi quelle delle slide, o i file *_generated.png se usi questi)."
    # )
