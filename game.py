import streamlit as st

# Initialize game state only once
if "board" not in st.session_state:
    st.session_state.board = [""] * 9
if "player" not in st.session_state:
    st.session_state.player = "X"
if "winner" not in st.session_state:
    st.session_state.winner = None

def check_winner(board):
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)               # diagonals
    ]
    for a, b, c in wins:
        if board[a] == board[b] == board[c] and board[a] != "":
            return board[a]
    return None

st.title("❌⭕ Tic Tac Toe (2 Players)")

cols = st.columns(3)
for i in range(9):
    if cols[i % 3].button(st.session_state.board[i] or " ", key=i):
        if st.session_state.board[i] == "" and st.session_state.winner is None:
            # Place current player's mark
            st.session_state.board[i] = st.session_state.player
            # Check winner
            st.session_state.winner = check_winner(st.session_state.board)
            # Switch player for next turn
            if st.session_state.winner is None:
                st.session_state.player = "O" if st.session_state.player == "X" else "X"

# Show status
if st.session_state.winner:
    st.success(f"🎉 Player {st.session_state.winner} wins!")
elif "" not in st.session_state.board:
    st.info("It's a draw!")
else:
    st.write(f"Next turn: Player {st.session_state.player}")

# Restart button
if st.button("Restart Game"):
    st.session_state.board = [""] * 9
    st.session_state.player = "X"
    st.session_state.winner = None
