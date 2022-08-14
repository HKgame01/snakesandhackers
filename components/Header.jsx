import styles from '../styles/Header.module.css'

export default function Header({ }) {
  return (
    <nav className={styles.nav}>
      <div className={styles.logo}>
        <a href="#">
          {/* <img src="/logo.png" alt="logo" /> */}
          To The Old Ways
        </a>
      </div>
      <div className={styles['menu-items']}>
        <a rel="noopener noreferrer" target="_blank" href="https://t.me/snakeandhackers_bot">Snakes & Ladder</a>
        <a rel="noopener noreferrer" target="_blank" href="https://t.me/gamingarena3_bot">Gaming Arena</a>
      </div>
    </nav>
  )
}