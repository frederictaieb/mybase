import { animate, createScope, createSpring, createDraggable } from 'animejs';
import { useEffect, useRef, useState } from 'react';
import reactLogo from './assets/react.svg';
import './App.css';

function App() {
  const root = useRef(null);
  const scope = useRef(null);
  const [ rotations, setRotations ] = useState(0);
  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchItems = async () => {
      try {
        setLoading(true);
        const response = await fetch('http://localhost:8000/items/');
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        setItems(data);
      } catch (e) {
        console.error('Erreur lors de la récupération des items:', e);
        setError(e.message);
      } finally {
        setLoading(false);
      }
    };

    fetchItems();

    scope.current = createScope({ root }).add( self => {
    
      // Every anime.js instances declared here are now scopped to <div ref={root}>

      // Created a bounce animation loop
      animate('.logo', {
        scale: [
          { to: 1.25, ease: 'inOut(3)', duration: 200 },
          { to: 1, ease: createSpring({ stiffness: 300 }) }
        ],
        loop: true,
        loopDelay: 250,
      });
      
      // Make the logo draggable around its center
      createDraggable('.logo', {
        container: [0, 0, 0, 0],
        releaseEase: createSpring({ stiffness: 200 })
      });

      // Register function methods to be used outside the useEffect
      self.add('rotateLogo', (i) => {
        animate('.logo', {
          rotate: i * 360,
          ease: 'out(4)',
          duration: 1500,
        });
      });

    });

    // Properly cleanup all anime.js instances declared inside the scope
    return () => scope.current.revert()

  }, []);

  const handleClick = () => {
    setRotations(prev => {
      const newRotations = prev + 1;
      // Animate logo rotation on click using the method declared inside the scope
      scope.current.methods.rotateLogo(newRotations);
      return newRotations;
    });
  };

  return (
    <div ref={root} className="container">
      <h1>Liste des Items</h1>
      
      {loading && <p>Chargement en cours...</p>}
      
      {error && <p className="error">Erreur: {error}</p>}
      
      {!loading && !error && (
        <div className="items-container">
          {items.length === 0 ? (
            <p>Aucun item trouvé</p>
          ) : (
            <ul className="items-list">
              {items.map(item => (
                <li key={item.id} className="item-card">
                  <h3>{item.name}</h3>
                  <p>ID: {item.id}</p>
                </li>
              ))}
            </ul>
          )}
        </div>
      )}

      <div className="large centered row">
        <img src={reactLogo} className="logo react" alt="React logo" />
      </div>
      <div className="medium row">
        <fieldset className="controls">
        <button onClick={handleClick}>rotations: {rotations}</button>
        </fieldset>
      </div>
    </div>
  )
}

export default App;