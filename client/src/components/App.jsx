import { Link, Route, Routes } from "react-router-dom";
import Camper from "./Camper";
import Home from "./Home";

function App() {

  const API_URL="http://localhost:5555"

  return (
    <main>
      <h1>
        <Link to="/">Camping Fun</Link>
      </h1>
      <Routes>
            <Route 
                path="/"
                element={<Home  API_URL={API_URL}/>}
            />
            <Route 
                path="/campers/:id"
                element={<Camper API_URL={API_URL}/>}
            />
      </Routes>
    </main>
  );
}

export default App;