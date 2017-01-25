import React from 'react'
import { connect } from 'react-redux'
import { bindActionCreators } from 'redux'

import { updateFilter } from '../reducers/projectsTableReducer'
import {
  SHOW_ALL,
  SHOW_NEW,
} from '../constants'


const FilterSelector = props =>
  <div style={{ display: 'inline' }}>
    <select
      name="filterSelector"
      value={props.filter}
      onChange={event => props.onChange(event.target.value)}
      style={{ width: '90px', display: 'inline', padding: '0px !important' }}
    >
      <option value={SHOW_ALL}>All</option>
      <option value={SHOW_NEW}>New</option>
    </select>
  </div>

FilterSelector.propTypes = {
  filter: React.PropTypes.string.isRequired,
  onChange: React.PropTypes.func.isRequired,
}

const mapStateToProps = state => ({ filter: state.projectsTable.filter })

const mapDispatchToProps = dispatch => bindActionCreators({ onChange: updateFilter }, dispatch)

export default connect(mapStateToProps, mapDispatchToProps)(FilterSelector)