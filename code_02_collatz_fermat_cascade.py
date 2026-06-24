# -*- coding: utf-8 -*-
"""code_02_collatz_fermat_cascade.ipynb
"""

# Collatz Dynamics: M-F Cascade Decay Diagram
# Hiroshi Harada
# June 24, 2026
# Released under the MIT License
# © 2026 Hiroshi Harada

from graphviz import Digraph

def generate_decay_diagram(filename='MF_Cascade_Decay'):
    dot = Digraph(comment='M-F Cascade Decay', format='png')
    dot.attr(rankdir='TB', splines='ortho', nodesep='0.8', ranksep='1.0')
    dot.attr('node', fontname='Helvetica, Arial, sans-serif')

    trajectory = [
        (1, 4, 5),
        (5, 3, 13),
        (13, 2, 17),
        (17, 1, 11),
        (11, 1, 7)
    ]

    # Root node
    dot.node('J_1', '1', shape='circle', style='filled', fillcolor='gold', penwidth='2', width='0.6')

    for a, k, next_a in trajectory:
        M = a * (2 ** k) - 1
        F = a * (2 ** k) + 1

        # Unique node IDs
        M_node = f"M_{a}_{k}"
        F_node = f"F_{a}_{k}"
        J_node = f"J_{a}"
        J_next_node = f"J_{next_a}"

        # M-type (Collatz)
        dot.node(M_node, f"M: {M}\n(3J)", shape='box', style='filled', fillcolor='lightblue', penwidth='2')
        dot.edge(J_node, M_node, xlabel=f" ×2^{k} - 1", fontcolor='blue')
        dot.node(J_next_node, str(next_a), shape='circle', style='filled', fillcolor='gold', penwidth='2', width='0.6')
        dot.edge(M_node, J_next_node, xlabel=" ÷3", color='blue', penwidth='2', fontcolor='blue')

        # F-type (Conjugate)
        dot.node(F_node, f"F: {F}\n(cJ)", shape='box', style='filled,dashed', fillcolor='#e0e0e0', color='#666666', fontcolor='#555555')
        dot.edge(J_node, F_node, xlabel=f" ×2^{k} + 1", color='#888888', style='dashed', fontcolor='#666666')

    dot.render(filename, view=False)
    print(f"[Success] Cascade diagram generated: {filename}.png")

if __name__ == '__main__':
    generate_decay_diagram()

