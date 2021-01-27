let $chapterSaveButton = document.querySelector('#chapter_save_button');
let $chapterTitle = document.querySelector('#chapter_title_input');
let $chapterContent = document.querySelector('#chapter_content_input');
let $novelId = document.querySelector('#novel_id');
let $chapterForm = document.querySelector('#new_chapter_form');

$chapterForm.addEventListener('submit', e => {
    let chapterContent = quill.root.innerHTML;

    $chapterContent.value = chapterContent;

});