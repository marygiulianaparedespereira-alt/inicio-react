
function Pelicula(props) {
const { año,titulo,vista } = props;

 return (
    <div>
      <p>{titulo} {vista && "listo"}</p>
      <h1>{año}</h1>
      
    </div>
  );
}
export default Pelicula;
