"use client"
import {useEffect,useState} from "react"

export default function Dashboard(){

const [portfolio,setPortfolio] = useState(null)

useEffect(()=>{

fetch("/api/portfolio/demo")
.then(r=>r.json())
.then(setPortfolio)

},[])

return(

<div style={{background:"#000",color:"#fff",minHeight:"100vh",padding:40}}>

<h1>Portfolio Dashboard</h1>

{portfolio && (

<div>

<h3>ETH Price</h3>
<p>{JSON.stringify(portfolio.eth_price)}</p>

<h3>SOL Price</h3>
<p>{JSON.stringify(portfolio.sol_price)}</p>

</div>

)}

</div>

)
}