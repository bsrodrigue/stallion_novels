$('#dark-mode-toggle-button').click(()=>{
    $('body').toggleClass('dark-mode-body');
    $('h1, a, p').toggleClass('dark-mode-text');
});