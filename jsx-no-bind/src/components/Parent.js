import * as React from 'react'

class RegularChildA extends React.Component {
  render() {
    console.log('render regular A')
    return (
      <div onClick={this.props.onClick}>{this.props.message}</div>
    )
  }
}

class RegularChildB extends React.Component {
  shouldComponentUpdate(nextProps, nextState) {
    return this.props.message !== nextProps.message
  }

  render() {
    console.log('render regular B')
    return (
      <div onClick={this.props.onClick}>{this.props.message}</div>
    )
  }
}

class PureChild extends React.PureComponent {
  handleClick = () => {
    this.props.onClick(this.props.message)
  }

  render() {
    console.log('render pure')
    return (
      <div onClick={this.handleClick} className={this.props.className}>{this.props.message}</div>
    )
  }
}

const StatelessChild = props => {
  console.log('render stateless')
  return (
    <div onClick={props.onClick}>{props.message}</div>
  )
}

export default class Parent extends React.Component {
  state = {
    count: 0,
  }

  increment = () => {
    this.setState(state => {
      return {
        count: state.count + 1,
        className: 'count-' + (state.count + 1),
      }
    })
  }

  handleClick = message => {
    console.log(message)
  }

  render() {
    return (
      <div style={{ lineHeight: '30px' }}>
        <h2>Example 1: Different Types of React Components</h2>
        <div>
          <button onClick={this.increment}>Add</button>
          &nbsp;&nbsp;
          Count: {this.state.count}
        </div>

        <div style={{ cursor: 'pointer' }}>
          <RegularChildA message="regular A" onClick={() => { console.log('reguler A') }} />
          <RegularChildB message="regular B" onClick={() => { console.log('regular B')}} />
          <PureChild message="pure" onClick={this.handleClick} />
          <StatelessChild message="stateless" onClick={() => { console.log('stateless') }} />
        </div>
      </div>
    )
  }
}
