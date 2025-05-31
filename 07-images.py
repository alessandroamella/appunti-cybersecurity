import os

import matplotlib.patches as patches
import matplotlib.pyplot as plt


def create_x509_diagram():
    # Dark theme colors
    bg_color = "#141414"  # Slightly off-black for page background
    text_color = "#E6E6E6"  # Slightly off-white for text
    box_color = "#323232"  # Dark gray for boxes
    line_color = "#B4B4B4"  # Lighter gray for lines/arrows
    highlight_color = "#64B4FF"  # Light blue for highlights

    fig, ax = plt.subplots(figsize=(12, 7))
    fig.patch.set_facecolor(bg_color)
    ax.set_facecolor(bg_color)

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.axis("off")

    # Helper to create styled text
    def add_text(
        x, y, text, size=10, color=text_color, ha="center", va="center", **kwargs
    ):
        ax.text(
            x,
            y,
            text,
            color=color,
            fontsize=size,
            ha=ha,
            va=va,
            family="sans-serif",
            **kwargs
        )

    # Helper to create styled boxes
    def add_box(
        x,
        y,
        w,
        h,
        label="",
        boxcolor=box_color,
        textcolor=text_color,
        labelcolor=text_color,
    ):
        rect = patches.Rectangle(
            (x, y),
            w,
            h,
            linewidth=1,
            edgecolor=line_color,
            facecolor=boxcolor,
            zorder=2,
        )
        ax.add_patch(rect)
        if label:
            add_text(x + w / 2, y + h / 2, label, color=textcolor, size=9)
        return x, y, w, h

    # Helper for arrows
    def add_arrow(start_x, start_y, end_x, end_y, color=line_color):
        ax.annotate(
            "",
            xy=(end_x, end_y),
            xytext=(start_x, start_y),
            arrowprops=dict(arrowstyle="->", color=color, lw=1.5),
            zorder=1,
        )

    # --- Create signed digital certificate (Left side) ---
    add_text(
        2.5,
        6.5,
        "Creazione Certificato Digitale Firmato (CA)",
        size=12,
        color=highlight_color,
        weight="bold",
    )

    # Unsigned certificate
    x_uc, y_uc, w_uc, h_uc = add_box(
        0.5, 4.5, 2.5, 1, "Certificato non firmato:\nID Utente, Chiave Pubblica Utente"
    )

    # Hash function
    x_h1, y_h1, w_h1, h_h1 = add_box(0.5 + (w_uc / 2) - 0.4, y_uc - 1.2, 0.8, 0.8, "H")
    add_arrow(x_uc + w_uc / 2, y_uc, x_h1 + w_h1 / 2, y_h1 + h_h1)
    add_text(
        x_h1 + w_h1 / 2,
        y_h1 - 0.3,
        "Genera hash del\ncertificato non firmato",
        size=8,
        va="top",
    )

    # Hash output
    x_hash_out, y_hash_out = x_h1 + w_h1 + 0.8, y_h1 + h_h1 / 2
    add_text(x_hash_out - 0.4, y_hash_out, "Hash", size=9, ha="right")

    # Sign function
    x_s, y_s, w_s, h_s = add_box(x_hash_out + 0.2, y_h1, 0.8, 0.8, "S")
    add_arrow(
        x_h1 + w_h1, y_h1 + h_h1 / 2, x_s, y_s + h_s / 2
    )  # from H to S (hash value)
    add_text(
        x_s + w_s / 2, y_s - 0.3, "Firma con chiave\nprivata della CA", size=8, va="top"
    )
    add_text(
        x_s - 0.3,
        y_s + h_s / 2 - 0.3,
        "Chiave Privata CA",
        size=7,
        ha="right",
        rotation=90,
        va="bottom",
    )
    # Simulate key icon
    key_priv_ca = patches.Circle(
        (x_s - 0.2, y_s - 0.5), 0.1, color=line_color, zorder=3
    )
    ax.add_patch(key_priv_ca)
    key_priv_ca_b = patches.Rectangle(
        (x_s - 0.22, y_s - 0.8), 0.04, 0.3, color=line_color, zorder=3
    )
    ax.add_patch(key_priv_ca_b)

    # Signed certificate (data block)
    add_box(
        0.5,
        1.0,
        4,
        1.2,
        "Certificato Firmato:\n"
        "ID Bob, Chiave Pubblica Bob\n"
        "Info CA, Info Certificato\n"
        "Firma Digitale",
        boxcolor=highlight_color,
        textcolor=bg_color,
    )

    # Arrow from Unsigned Cert to Signed Cert (showing data included)
    ax.plot(
        [x_uc + w_uc, x_uc + w_uc, 3, 3],
        [y_uc + h_uc / 2, 3.5, 3.5, 1.0 + 1.2],
        color=line_color,
        lw=1.0,
        linestyle="--",
    )
    # Arrow from Sign to Signed Cert (showing signature included)
    add_arrow(
        x_s + w_s, y_s + h_s / 2, 3, 1.0 + 1.2 / 2
    )  # Signature to signed cert block

    # --- Use verified certificate (Right side) ---
    add_text(
        7.5,
        6.5,
        "Utilizzo Certificato Verificato (Utente)",
        size=12,
        color=highlight_color,
        weight="bold",
    )

    # Signed Certificate (input for user)
    x_sc_in, y_sc_in, w_sc_in, h_sc_in = add_box(
        6,
        4.5,
        3,
        1.2,
        "Certificato Firmato\n(ricevuto da Bob)",
        boxcolor=highlight_color,
        textcolor=bg_color,
    )

    # Hash function (for verification)
    x_h2, y_h2, w_h2, h_h2 = add_box(
        6 - 1.2, y_sc_in + h_sc_in / 2 - 0.4, 0.8, 0.8, "H"
    )
    # Data part of signed cert goes to H
    ax.plot(
        [x_sc_in, x_sc_in - 0.5, x_sc_in - 0.5, x_h2 + w_h2],
        [
            y_sc_in + h_sc_in * 0.7,
            y_sc_in + h_sc_in * 0.7,
            y_h2 + h_h2 / 2,
            y_h2 + h_h2 / 2,
        ],
        color=line_color,
        lw=1.0,
        linestyle="-",
    )
    add_text(x_h2 - 0.3, y_h2 + h_h2 / 2 + 0.2, "Parte dati", size=7, ha="right")

    # Verify function
    x_v, y_v, w_v, h_v = add_box(
        x_sc_in + w_sc_in / 2 - 0.4, y_sc_in - 1.2, 0.8, 0.8, "V"
    )
    # Signature part of signed cert goes to V
    ax.plot(
        [
            x_sc_in + w_sc_in * 0.8,
            x_sc_in + w_sc_in * 0.8,
            x_v + w_v / 2,
            x_v + w_v / 2,
        ],
        [y_sc_in, y_sc_in - 0.4, y_sc_in - 0.4, y_v + h_v],
        color=line_color,
        lw=1.0,
        linestyle="-",
    )
    add_text(x_v + w_v / 2 + 0.1, y_sc_in - 0.2, "Firma", size=7, ha="left", va="top")

    # Hash from H2 to V
    add_arrow(x_h2, y_h2 + h_h2 / 2, x_v, y_v + h_v / 2)

    add_text(
        x_v + w_v / 2,
        y_v - 0.3,
        "Verifica firma\ncon chiave pubblica CA",
        size=8,
        va="top",
    )
    add_text(
        x_v + w_v + 0.3,
        y_v + h_v / 2 - 0.3,
        "Chiave Pubblica CA",
        size=7,
        ha="left",
        rotation=-90,
        va="bottom",
    )
    # Simulate key icon
    key_pub_ca = patches.Circle(
        (x_v + w_v + 0.2, y_v - 0.5), 0.1, color=line_color, zorder=3
    )
    ax.add_patch(key_pub_ca)
    key_pub_ca_b = patches.Rectangle(
        (x_v + w_v + 0.18, y_v - 0.8), 0.04, 0.3, color=line_color, zorder=3
    )
    ax.add_patch(key_pub_ca_b)

    # Verification result
    add_arrow(x_v + w_v / 2, y_v, x_v + w_v / 2, y_v - 0.8)
    add_text(
        x_v + w_v / 2,
        y_v - 1.1,
        "Algoritmo di verifica\nindica se la firma è valida",
        size=9,
    )

    # Output: Bob's Public Key
    add_arrow(
        x_sc_in + w_sc_in / 2,
        y_sc_in - (1.2 + 0.8 + 0.8 + 0.3),
        x_sc_in + w_sc_in / 2,
        1.0,
    )  # From below verification text
    add_text(
        x_sc_in + w_sc_in / 2,
        0.7,
        "Usa certificato verificato per\nottenere la chiave pubblica di Bob",
        size=9,
        va="top",
    )
    add_box(
        x_sc_in + w_sc_in / 2 - 1,
        0.1,
        2,
        0.6,
        "Chiave Pubblica di Bob",
        boxcolor=highlight_color,
        textcolor=bg_color,
    )

    # Create images directory if it doesn't exist
    if not os.path.exists("images"):
        os.makedirs("images")

    plt.savefig(
        "images/x509_process.png", facecolor=bg_color, bbox_inches="tight", dpi=150
    )
    print("Generated images/x509_process.png")


if __name__ == "__main__":
    create_x509_diagram()
