import React, { useEffect, useState } from 'react'


function loadTweets(callback) {
    const xhr = new XMLHttpRequest() 
    const method = "GET"
    const url = "http://localhost:8000/api/tweets/"
    const responseType = "json"
    xhr.responseType = responseType
    xhr.open(method, url)
    xhr.onload = function() {
       callback(xhr.response, xhr.status)
    }
    xhr.onerror = function (e) {
      console.log(e)
      callback({"message": "The request was an error"}, 400)
    }
    xhr.send()
  }

export function TweetsList(props){
    const [tweets, setTweets] = useState([])
  
    useEffect(() => {
      const myCallback = (response, status) => {
        if (status === 200){
          setTweets(response)
        } else {
          alert("There was an error")
        }
      }
      loadTweets(myCallback)
    }, [])
    return tweets.map((item, index)=>{
      return <Tweet tweet={item} className='my-5 py-5 border bg-white text-dark' key={`${index}-{item.id}`}/>
    })
  }

export function ActionBtn(props) {
    const {tweet, action} = props
    const className = props.className ? props.className : 'btn btn-primary'
    return action.type === "like" ? <button className={className}>{tweet.likes}Likes</button> : null
  }
  
export function Tweet(props) {
    const {tweet} = props
    const className = props.className ? props.className : 'col-10 mx-auto col-md-6'
    const like = {type:"like"}
    const unlike = {type:"like"}
    const retweet = {type:"like"}
    return <div className={className}>
        <p>{tweet.id} - {tweet.content}</p>
        <div className = 'btn btn-group'>
          <ActionBtn tweet={tweet} action={like}/>
        </div>
    </div>
  }