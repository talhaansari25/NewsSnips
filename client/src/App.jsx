import { Routes, Route } from 'react-router-dom';
import News from './components/News';
import NewsDetails from './components/NewsDetails';

const App = () => {
  return (
    <div>
      <Routes>
        <Route path="/" element={<News />} />
        <Route path="/newsdetails" element={<NewsDetails />} />
      </Routes>
    </div>
  );
};

export default App;
