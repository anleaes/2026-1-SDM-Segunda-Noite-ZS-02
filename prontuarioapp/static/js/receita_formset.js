document.addEventListener('DOMContentLoaded', function () {

    const addButton = document.getElementById('add-form');

    const totalForms = document.getElementById(
        'id_detalhes_medicamentos-TOTAL_FORMS'
    );

    const formContainer = document.getElementById(
        'formset-container'
    );

    addButton.addEventListener('click', function () {

        const currentFormCount = parseInt(totalForms.value);

        const firstForm = document.querySelector('.medicamento-form');

        const newForm = firstForm.cloneNode(true);

        newForm.innerHTML = newForm.innerHTML.replace(
            /detalhes_medicamentos-0-/g,
            `detalhes_medicamentos-${currentFormCount}-`
        );

        const inputs = newForm.querySelectorAll(
            'input, select, textarea'
        );

        inputs.forEach(input => {

            if (input.type !== 'hidden') {

                input.value = '';

            }

        });

        formContainer.appendChild(newForm);

        totalForms.value = currentFormCount + 1;

    });

});