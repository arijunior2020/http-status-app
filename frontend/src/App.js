import React, { useState, useEffect } from 'react';
import { motion } from 'framer-motion'; // Importação do Framer Motion

function App() {
    const [statusCodes, setStatusCodes] = useState([]);
    const [search, setSearch] = useState('');

    useEffect(() => {
        fetch(process.env.REACT_APP_BACKEND_URL || 'http://localhost:5000/status')
            .then((response) => response.json())
            .then((data) => setStatusCodes(data))
            .catch((error) => console.error('Erro ao buscar dados:', error));
    }, []);

    const filteredStatusCodes = statusCodes.filter((status) =>
        status.name.toLowerCase().includes(search.toLowerCase()) ||
        status.code.toString().includes(search)
    );

    return (
        <div className="min-h-screen bg-primary text-white p-6">
            {/* Adicionando o motion.div com animação */}
            <motion.div
                initial={{ opacity: 0, y: -20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.5 }}
            >
                <h1 className="text-4xl font-bold text-center mb-8 text-accent">
                    HTTP Status Codes
                </h1>
            </motion.div>

            <input
                type="text"
                placeholder="Buscar por código ou nome"
                value={search}
                onChange={(e) => setSearch(e.target.value)}
                className="w-full mb-6 p-3 rounded-md bg-secondary text-primary outline-none focus:ring-2 focus:ring-accent"
            />
            <div className="overflow-auto">
                <table className="w-full text-left border-collapse bg-secondary rounded-lg shadow-lg">
                    <thead className="bg-accent text-white">
                        <tr>
                            <th className="px-4 py-2">Código</th>
                            <th className="px-4 py-2">Nome</th>
                            <th className="px-4 py-2">Descrição</th>
                        </tr>
                    </thead>
                    <tbody>
                        {filteredStatusCodes.map((status, index) => (
                            <tr
                                key={status.code}
                                className={index % 2 === 0 ? 'bg-primary' : 'bg-gray-800'}
                            >
                                <td className="px-4 py-2">{status.code}</td>
                                <td className="px-4 py-2">{status.name}</td>
                                <td className="px-4 py-2">{status.description}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </div>
    );
}

export default App;
