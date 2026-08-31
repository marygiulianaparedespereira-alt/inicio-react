function Perfil(props) {
  const { nombre, rol, lenguajes } = props;

  console.log(lenguajes);
  return (
    <div>
      <h1>{nombre}</h1>
      <p>{rol}</p>
      <ul >
        {lenguajes.map((lenguaje, index) => (
          <li>{lenguaje}</li>
        ))}
      </ul>
    </div>
  );
}
export default Perfil;
