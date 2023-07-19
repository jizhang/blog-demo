import * as React from 'react'

export default class NoArgument extends React.Component {
  state = {
    count: 0,
  }

  constructor() {
    super()

    this.handleClickBoundA = this.handleClickUnbound.bind(this)

    this.handleClickBoundC = () => {
      this.setState(state => ({
        count: state.count + 1,
      }))
    }
  }

  handleClickUnbound() {
    this.setState(state => ({
      count: state.count + 1,
    }))
  }

  handleClickBoundB = () => {
    this.setState(state => ({
      count: state.count + 1,
    }))
  }

  render() {
    return (
      <div style={{ lineHeight: '30px' }}>
        <h2>Example 2: Event Handler Functions</h2>
        <div>Count: {this.state.count}</div>

        <button onClick={() => {
          this.setState(state => ({
            count: state.count + 1,
          }))
        }}>ArrowA</button>

        <button onClick={() => { this.handleClickUnbound() }}>
          ArrowB
        </button>

        <button onClick={this.handleClickUnbound.bind(this)}>
          Bind
        </button>

        <button onClick={this.handleClickBoundA}>BoundA</button>
        <button onClick={this.handleClickBoundB}>BoundB</button>
        <button onClick={this.handleClickBoundC}>BoundC</button>
      </div>
    )
  }
}
