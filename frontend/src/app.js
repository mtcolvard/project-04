import React from 'react'
import ReactDOM from 'react-dom'


import { HashRouter, Route, Switch } from 'react-router-dom'
// import { ToastContainer } from 'react-toastify'

import Home from './components/pages/Home'
import CrewIndex from './components/crews/CrewIndex'
import Navbar from './components/common/Navbar'


// import 'react-toastify/dist/ReactToastify.css'
// import '@fortawesome/fontawesome-free/js/all.js'
import 'bulma'
import './style.scss'


class App extends React.Component {


  render(){
    return(
      <div>
        <HashRouter>
          <Navbar />
          <Switch>
            <Route path="/crews" component={CrewIndex} />
            <Route path="/" component={Home} />
          </Switch>
        </HashRouter>
      </div>
    )
  }
}


ReactDOM.render(
  <App />,
  document.getElementById('root')
)
