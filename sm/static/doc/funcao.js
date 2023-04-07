// declaring variables
let selecionado = 0;
let astro1 = "";
let astro1texto = "";
let astro2 = "";
let astro2texto = "";

// function to show mixed images and clear them back
function handleSelection(event) {
    if (selecionado < 1) {
        // selecting first person to mix
        astro1 = $(this).find('.title').attr('id');
        astro1texto = document.getElementById(astro1).innerHTML

        // writing first part of the result
        document.getElementById("result").innerHTML = astro1texto + " x ?:";
        selecionado = 1;
    } else if (selecionado > 1) {
        // making everything back to new selection
        for (let i = 0; i < 8; i++) {
            $("#mixed" + (i + 1)).attr ("src", "");
        }
        selecionado = 0;
        handleSelection.call(this, event);
    } else {
        // selecting second person to mix
        astro2 = $(this).find('.title').attr('id');
        astro2texto = document.getElementById(astro2).innerHTML

        // preventing selection of same person
        if (astro1 != astro2) {
            // writing second part of the result
            document.getElementById("result").innerHTML = astro1texto + " x " + astro2texto + ":";

            // showing mixed images on page
            for (let i = 0; i < mixes.length; i++) {
                if (mixes[i].includes(astro1) && mixes[i].includes(astro2)) {
                    for (let j = 0; j < list_mixes[i].length; j++) {
                        $("#mixed" + (j + 1)).attr ("src", "static/img/mixed/" + mixes[i] + "/" + list_mixes[i][j]);
                    }
                }
            }
            selecionado = 2;
        }
    }
}

// setting up function
$(document).ready(function() {
    $('.select').on('click', handleSelection);
});
