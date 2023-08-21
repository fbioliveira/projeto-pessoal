let circularProgress = document.querySelector('.circular-progress'),
    progressValue = document.querySelector('.progress-value')

let progressStartValue = 0,
    element = document.getElementById('percentual-loja-regiao-um').innerHTML,
    progressEndValue = element,
    speed = 30;
    

let progress = setInterval(() => {
    if (progressEndValue > 0){
        progressStartValue++
        
        progressValue.textContent = `${progressStartValue}%`
        circularProgress.style.background = `conic-gradient(#069aef ${progressStartValue * 3.6}deg, #ededed 0deg)`
    }

    if(progressStartValue == progressEndValue){
        clearInterval(progress);
    }
}, speed);
// -----------------------------------------------------------------------------------------------------------------------------
let circularProgressDois = document.querySelector('.circular-progress-dois'),
    progressValueDois = document.querySelector('.progress-value-dois')

let progressStartValueDois = 0,
    elementDois = document.getElementById('percentual-loja-regiao-dois').innerHTML,
    progressEndValueDois = elementDois,
    speedDois = 30;
    

let progressDois = setInterval(() => {
    if (progressEndValueDois > 0){
        progressStartValueDois++
        
        progressValueDois.textContent = `${progressStartValueDois}%`
        circularProgressDois.style.background = `conic-gradient(#069aef ${progressStartValueDois * 3.6}deg, #ededed 0deg)`
    }

    if(progressStartValueDois == progressEndValueDois){
        clearInterval(progressDois);
    }
}, speedDois);
// -----------------------------------------------------------------------------------------------------------------------------------
let circularProgressGeral = document.querySelector('.circulo-geral'),
    progressValueGeral = document.querySelector('.progress-value-geral')

let progressStartValueGeral = 0,
    elementGeral = document.getElementById('percentual-loja-geral').innerHTML,
    progressEndValueGeral = elementGeral,
    speedGeral = 30;

let progressGeral = setInterval(() => {
    if (elementGeral > 0){
        progressStartValueGeral++
        
        progressValueGeral.textContent = `${progressStartValueGeral}%`
        circularProgressGeral.style.background = `conic-gradient(#a41f08 ${progressStartValueGeral * 3.6}deg, #ededed 0deg)`
    }

    if(progressStartValueGeral == progressEndValueGeral){
        clearInterval(progressGeral);
    }
}, speedGeral);
// -------------------------------------------------------------------------------------------------------------------------------------
let circularProgressManutencao = document.querySelector('.circulo-manutencao'),
    progressValueManutencao = document.querySelector('.progresso-manutencao')

let progressStartValueManutencao = 0,
    elementManutencao = document.getElementById('percentual-equipe-manutencao').innerHTML,
    progressEndValueManutencao = elementManutencao,
    speedManutencao = 30;
    

let progressManutencao = setInterval(() => {
    if (elementManutencao > 0){
        progressStartValueManutencao++
        
        progressValueManutencao.textContent = `${progressStartValueManutencao}%`
        circularProgressManutencao.style.background = `conic-gradient(#a41f08 ${progressStartValueManutencao * 3.6}deg, #ededed 0deg)`
    }

    if(progressStartValueManutencao == progressEndValueManutencao){
        clearInterval(progressManutencao);
    }
}, speedManutencao);
// ----------------------------------------------------------------------------------------------------------------------------------------


let manutencaoClassUm = document.querySelector('.manutencao-regiao')
let manutencaoClassDois = document.querySelector('.manutencao-dois')




