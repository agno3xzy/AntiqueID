/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.entity;

import java.io.Serializable;
import javax.persistence.Basic;
import javax.persistence.Column;
import javax.persistence.Embeddable;
import javax.validation.constraints.NotNull;
import javax.validation.constraints.Size;

/**
 *
 * @author agno3
 */
@Embeddable
public class ClassificationPK implements Serializable {

    @Basic(optional = false)
    @NotNull
    @Size(min = 1, max = 200)
    @Column(name = "class_id")
    private String classId;
    @Basic(optional = false)
    @NotNull
    @Column(name = "user_user_id")
    private int userUserId;

    public ClassificationPK() {
    }

    public ClassificationPK(String classId, int userUserId) {
        this.classId = classId;
        this.userUserId = userUserId;
    }

    public String getClassId() {
        return classId;
    }

    public void setClassId(String classId) {
        this.classId = classId;
    }

    public int getUserUserId() {
        return userUserId;
    }

    public void setUserUserId(int userUserId) {
        this.userUserId = userUserId;
    }

    @Override
    public int hashCode() {
        int hash = 0;
        hash += (classId != null ? classId.hashCode() : 0);
        hash += (int) userUserId;
        return hash;
    }

    @Override
    public boolean equals(Object object) {
        // TODO: Warning - this method won't work in the case the id fields are not set
        if (!(object instanceof ClassificationPK)) {
            return false;
        }
        ClassificationPK other = (ClassificationPK) object;
        if ((this.classId == null && other.classId != null) || (this.classId != null && !this.classId.equals(other.classId))) {
            return false;
        }
        if (this.userUserId != other.userUserId) {
            return false;
        }
        return true;
    }

    @Override
    public String toString() {
        return "com.entity.ClassificationPK[ classId=" + classId + ", userUserId=" + userUserId + " ]";
    }
    
}
