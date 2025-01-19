import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const NewsComp2 = () => {
  const [newsList, setNewsList] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchRandomNews = async () => {
      try {
        const response = await axios.get('http://localhost:5000/all');
        const shuffledArticles = shuffleArray(response.data.output);
 
        const filteredArticles = shuffledArticles.filter(article => article.url_to_image);
        setNewsList(filteredArticles.slice(31, 60)); 
        setLoading(false);
      } catch (err) {
        console.error('Error fetching news:', err);
        setError('Failed to load news articles');
        setLoading(false);
      }
    };

    fetchRandomNews();
  }, []);

  const shuffleArray = (array) => {
    for (let i = array.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
  };

  const handleNewsClick = async (newsItem) => {
    try {
      setLoading(true);
      const summaryResponse = await axios.post("http://localhost:5000/summary", {
        bigText: newsItem.full_content,
      });
      navigate("/newsdetails", {
        state: { newsItem, summary: summaryResponse.data.output },
      });
      setLoading(false);
    } catch (error) {
      console.error("Error fetching summary:", error);
      setLoading(false);
    }
  };

  if (loading) return <div className='loader'></div>;
  if (error) return <div>{error}</div>;

  return (
    <div className='newsComp2'>

      <div className='newsComp2-scrollable-container'>
        {newsList.map((article, index) => (
          <div className='newsComp2-item' key={index} onClick={() => handleNewsClick(article)}>
            <img src={article.url_to_image} alt={article.title} className='newsComp2-image' />
            <div className='newsComp2-item-title'>{article.title}</div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default NewsComp2;
