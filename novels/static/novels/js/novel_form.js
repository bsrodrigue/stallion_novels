let $novelDescription = document.querySelector('#novel_description_input');
let $form = document.querySelector('#novel_form');

$form.addEventListener('submit', e => {
    let novelDescription = quill.root.innerHTML;

    $novelDescription.value = novelDescription;
});