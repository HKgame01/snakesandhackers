import type { NextPage } from 'next'
import Head from 'next/head'
import Image from 'next/image'
import Header from '../components/Header'

const Home: NextPage = () => {
  return (
    <div>
      <Head>
        <title>To the old Ways</title>
        <meta name="description" content="To the old ways" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <Header />
      <section className="hero">
        <a href="#snake-and-ladder">
          <button className="know-more">
            Know more
          </button>
        </a>
      </section>
      <section id="snake-and-ladder" className="snake-and-ladder">
        <div className="section-left">
          <p>
            100 squares full of traps and tricks…Roll the dice and try your luck!
            Ladders will take you up but Snakes will take you down! Are you afraid of serpents?
            No problem! This game is two versions in one — just choose your game mode.
            You can play against a computer, or two players can
            compete against each other. <a target="_blank" rel="noopener noreferrer" href="https://t.me/snakeandhackers_bot">Play now</a>
          </p>
        </div>
        <div className="section-right">
          <img src="/snake.png" alt="Snake and Ladder" />
        </div>
      </section>

      <footer className="footer">
        Copyright © SnakeGame 2022
      </footer>
    </div>
  )
}

export default Home
