import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const NewsComponent = () => {
  const [newsList, setNewsList] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [currentIndex, setCurrentIndex] = useState(0); 
  const navigate = useNavigate();

  useEffect(() => {
    const fetchRandomNews = async () => {
      try {
        const response = await axios.get('http://localhost:5000/all'); 
        const articles = response.data.output; 
        console.log(articles);
        
        const shuffledArticles = shuffleArray(articles);
        const randomArticles = shuffledArticles.slice(0, 30); 
        
        const filteredArticles = randomArticles.filter(article => article.url_to_image !== "");
        
        setNewsList(filteredArticles);
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

  const handleNext = () => {
    setCurrentIndex((prevIndex) => (prevIndex + 1) % newsList.length); 
  };

  const handlePrevious = () => {
    setCurrentIndex((prevIndex) => (prevIndex - 1 + newsList.length) % newsList.length); 
  };

  if (loading) return <div className='loader'></div>;
  if (error) return <div>{error}</div>;

  const currentArticle = newsList[currentIndex];

  return (
    <div className='newsFeedB'>
      <div className="button-container">

      </div>
      {currentArticle && (
        <div className="news-item" onClick={() => handleNewsClick(currentArticle)}>
          {currentArticle.url_to_image && ( 
            <img src={currentArticle.url_to_image} alt={currentArticle.title} />
          )}
          <div className="news-title">{currentArticle.title}</div>
        </div>
      )}
      <div className="button-container">
        <button onClick={handlePrevious}>Previous</button>
        <button onClick={handleNext}>Next</button>
      </div>
    </div>
  );
};

export default NewsComponent;
