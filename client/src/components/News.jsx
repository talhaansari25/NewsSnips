import React, { useState } from "react";
import axios from "axios";
import Modal from "react-modal";
import { useNavigate } from "react-router-dom";
import NewsComp from './NewsComp';
import NewsComp2 from './NewsComp2';

const News = () => {
  const [keyword, setKeyword] = useState("");
  const [category, setCategory] = useState(""); 
  const [newsList, setNewsList] = useState([]);
  const [modalIsOpen, setModalIsOpen] = useState(false);
  const navigate = useNavigate();
  const [loading, setLoading] = useState(false);

  const handleSearch = async () => {
    setLoading(true);
    try {
      const response = await axios.post("http://localhost:5000/search", {
        query: keyword,
      });
      setNewsList(response.data.output);
      setModalIsOpen(true);
    } catch (error) {
      console.error("Error fetching news:", error);
    } finally {
      setLoading(false);
      setKeyword("");
    }
  };

  const handleCategorySelect = async () => {
    if (!category) return;
    setLoading(true);
    try {
      const response = await axios.post("http://localhost:5000/category", {
        catList: [category], 
      });
      setNewsList(response.data.output);
      setModalIsOpen(true);
    } catch (error) {
      console.error("Error fetching news by category:", error);
    } finally {
      setLoading(false);
      setCategory(""); 
    }
  };

  if (loading) return <div className="loader"></div>;

  const handleNewsClick = async (newsItem) => {
    try {
      const summaryResponse = await axios.post("http://localhost:5000/summary", {
        bigText: newsItem.full_content,
      });
      navigate("/newsdetails", {
        state: { newsItem, summary: summaryResponse.data.output },
      });
    } catch (error) {
      console.error("Error fetching summary:", error);
    }
  };

  return (
    <>
      <div className="navbarT">
        <h1>NewsSnips</h1>

        <div className="searchB">
          <input
            type="text"
            placeholder="Search News"
            value={keyword}
            onChange={(e) => setKeyword(e.target.value)}
          />
          <i className="fas fa-search" onClick={handleSearch}></i>
        </div>

        <select value={category} onChange={(e) => setCategory(e.target.value)}>
          <option value="">Select Categories</option>
          <option value="Sports">Sports</option>
          <option value="Politics">Politics</option>
          <option value="Technology">Technology</option>
          <option value="Health">Health</option>
          <option value="Science">Science</option>
          <option value="History">History</option>
        </select>
        <button className="newsBK" onClick={handleCategorySelect}>Search by Category</button> 

        <Modal
          isOpen={modalIsOpen}
          onRequestClose={() => setModalIsOpen(false)}
          ariaHideApp={false}
          style={{
            content: {
              backgroundColor: "var(--light)",
              color: "var(--text)",
              borderRadius: "8px",
              padding: "20px",
              maxWidth: "70%",
              maxHeight: "90vh",
              margin: "auto",
              boxShadow: "0 4px 20px rgba(0, 0, 0, 0.2)",
              border: "none",
            },
            overlay: {
              backgroundColor: "rgba(0, 0, 0, 0.75)",
            },
          }}
        >
          <div className="sF">
            <h2>Search Results</h2>
            <i className="fas fa-close" onClick={() => setModalIsOpen(false)}></i>
          </div>
          <ul>
            {newsList.map((newsItem, index) => (
              <li className="kaisa" key={index} onClick={() => handleNewsClick(newsItem)}>
                <img src={newsItem.url_to_image} alt={newsItem.title} />
                <h3>{newsItem.title}</h3>
              </li>
            ))}
          </ul>
        </Modal>
      </div>

      <div className="flexNC">
        <NewsComp />
        <NewsComp2 />
      </div>
    </>
  );
};

export default News;
