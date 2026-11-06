import { Link, Route, Routes } from "react-router-dom";
import Camper from "./Camper";
import Home from "./Home";

function App() {
  return (
    <main>
      <h1>
        <Link to="/">Camping Fun</Link>
      </h1>
      <Routes>
            <Route 
                path="/"
                element={<Home />}
            />
            <Route 
                path="/campers/:id"
                element={<Camper />}
            />
      </Routes>
    </main>
  );
}

export default App;