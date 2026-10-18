
const buttons = document.querySelectorAll(".cell");
const startBtn = document.querySelector(".startBtn");
const resetBtn = document.querySelector(".resetBtn");
const message = document.querySelector("#message");

const winning = [  //All possible winning combinations using button indexes
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],

    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],

    [0, 4, 8],
    [2, 4, 6]
];

let current_player = "X";  // Set the initial player and game status
let game_started = false;

startBtn.addEventListener("click", () => {     //Start the game when the Start button is clicked
    game_started = true;  
    message.textContent = current_player + "'s Turn";

    buttons.forEach((button) => {

        button.addEventListener("click", () => {

            if (!game_started){   //Prevent moves if the game has not started or has ended
                return;
            } 

            if (button.textContent !== "") {   // Prevent players from overwriting an occupied cell
                return;
            }

            button.textContent = current_player;

            Winner();

            if (!game_started){  //Stops here if a player wins or the game ends in a draw
                return;
            }

            if (current_player === "X") {
                current_player = "O";
            } else {
                current_player = "X";
            }

            message.textContent = current_player + "'s Turn";
        });

    });
});

resetBtn.addEventListener("click", () => {   // Reset the board and prepare the game for a new start
    buttons.forEach((button) => {
        button.textContent = "";
    });

    current_player = "X";
    game_started = false;
    message.textContent = "Click Start to play!";
});

function Winner() {   //Check all possible winning cominations
    for (let i = 0; i < winning.length; i++) {

        let a = winning[i][0];  //Get the three cell indexes for the current combination
        let b = winning[i][1];
        let c = winning[i][2];

        if (
            buttons[a].textContent === "X" &&
            buttons[b].textContent === "X" &&
            buttons[c].textContent === "X"
        ) {
            message.textContent = "Winner is X!";
            game_started = false;
            return;
        }

        if (
            buttons[a].textContent === "O" &&
            buttons[b].textContent === "O" &&
            buttons[c].textContent === "O"
        ) {
            message.textContent = "Winner is O!";
            game_started = false;
            return;
        }
    }

    let draw = true;

    buttons.forEach((button) => {   //Assume the game is a draw until an empty cell is found
        if (button.textContent === "") {
            draw = false;
        }
    });

    if (draw) {   //If every cell is filled and nobody won, declare a draw
        message.textContent = "It's a draw!";
        game_started = false;
    }
}
