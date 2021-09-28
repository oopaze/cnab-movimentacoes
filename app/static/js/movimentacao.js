function activeItem(id, data){
    var items = document.querySelectorAll(".item")  
    items.forEach((item) => { 
        if (item.getAttribute("item-data") === id){
            item.classList.add("active") 
            writeData(data)
        } else {
            item.classList.remove("active") 
        }
    })
}

function writeData(data){
    document.querySelector(".item-foco .item #numero").innerText = data.object.cartao
    document.querySelector(".item-foco .item #valor").innerText = `R$ ${data.object.valor}`
    document.querySelector(".item-foco .item #cpf").innerText = data.object.cpf
    document.querySelector(".item-foco .item #destinatario").innerText = data.object.dono_loja
    document.querySelector(".item-foco .item #local-compra").innerText = data.object.nome_loja
    document.querySelector(".item-foco .item #data-compra").innerText = data.object.data
    document.querySelector(".item-foco .item #natureza").innerText = data.object.natureza
    document.querySelector(".item-foco .item #saidas_value").innerText = `R$ ${data.object.pago}`
    document.querySelector(".item-foco .item #entradas_value").innerText = `R$ ${data.object.recebido}`
    document.querySelector(".item-foco .item #saldo").innerText = `R$ ${data.object.saldo}`

    if (data.object.natureza === 'saida'){
        document.querySelector("#label_valor").innerText = "Valor Pago"
    } else {
        document.querySelector("#label_valor").innerText = "Valor Recebido"
    }
}

async function getMoreDetails(id){
    return await fetch(`/${id}/`, {
        method: 'GET'
    }).then(
        (response) => response.json()
    ).then((data) => {
        return data
    })
}

const items = document.querySelectorAll(".item")
items.forEach(function(item) {
    let id = item.getAttribute("item-data")
    item.addEventListener("click", async function(e) { 
        let data = await getMoreDetails(id)
        if(data.success){
            activeItem(id, data)
        }
    })
})