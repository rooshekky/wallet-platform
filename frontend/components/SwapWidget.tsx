export default function SwapWidget(){

return(

<div style={{background:"#111",padding:20,borderRadius:10}}>

<h2>Swap Tokens</h2>

<input placeholder="Token In" style={{display:"block",marginBottom:10}}/>

<input placeholder="Token Out" style={{display:"block",marginBottom:10}}/>

<input placeholder="Amount" style={{display:"block",marginBottom:10}}/>

<button>Swap</button>

</div>

)
}