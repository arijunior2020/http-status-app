import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import './styles.css';

// Renderiza o componente principal (App) na div com o id "root" definida no index.html
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <React.StrictMode>
        <App />
    </React.StrictMode>
);
